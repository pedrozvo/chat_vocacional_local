import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_val_score
from database import load_data

MODEL_NAME = "modelo_vocacional.joblib"

def train_optimized_model():
    """
    Búsqueda de hiperparámetros optimizados para mejorar la precisión.
    Prueba diferentes configuraciones de vectorización y parámetros del algoritmo.
    """
    df = load_data()
    
    if len(df) < 5:
        return {"status": "error", "message": "Se necesitan al menos 5 datos para optimizar."}

    # Pipeline con TF-IDF (mejor que CountVectorizer para este caso)
    pipeline = Pipeline([
        ('vect', TfidfVectorizer(lowercase=True, stop_words='spanish')),
        ('clf', MultinomialNB()),
    ])

    # Definir parámetros a optimizar
    parameters = {
        'vect__max_features': [50, 100, 200],
        'vect__ngram_range': [(1, 1), (1, 2)],
        'clf__alpha': [0.1, 0.5, 1.0],
    }

    # Configurar búsqueda con validación cruzada adaptativa
    cv_folds = min(3, len(df) // 2) if len(df) > 3 else 2
    grid_search = GridSearchCV(
        pipeline,
        parameters,
        cv=cv_folds,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )
    
    try:
        grid_search.fit(df['texto'], df['categoria'])
        best_model = grid_search.best_estimator_
        best_score = grid_search.best_score_
    except (ValueError, Exception) as e:
        # Fallback con parámetros por defecto
        pipeline.fit(df['texto'], df['categoria'])
        best_model = pipeline
        best_score = cross_val_score(
            pipeline,
            df['texto'],
            df['categoria'],
            cv=cv_folds,
            scoring='accuracy'
        ).mean()

    # Guardar el mejor modelo
    joblib.dump(best_model, MODEL_NAME)

    return {
        "status": "success",
        "message": "Modelo Optimizado Exitosamente",
        "best_params": dict(grid_search.best_params_) if hasattr(grid_search, 'best_params_') else "Parámetros por defecto",
        "best_score": round(best_score, 3),
        "samples_trained": len(df)
    }