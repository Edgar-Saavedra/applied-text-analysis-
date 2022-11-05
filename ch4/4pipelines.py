# Pipelines
# Often a series of transformers on raw data until it passes to the fit method of a final estimator. 
# Scikit-Learn `Pipeline` Object is a solution.`

# Pipeline enables us to intgrate a series of transformers
# - combine normalization, vectorization and feature analysis into 1 single mechanism
# - Pipeline move data from a loader (object that will wrap our CorpusReader) into feature extraction mechanisms
# - To finally an estimator object that implements our models
# Data > Loader (CorpusReader) > Feature Extraction > Estimator
# Pipelines are "directed acyclic graphs (DAGs)", simple linear chains of transformers to arbitrarily complex branching and joining graphs

# Basics:
# purpose to chain multiple estimators representing a fixed sequence of steps into a single unit.
# - All estimators except last must be tranformers, implement the `transform` method
# - Estimators can be of any type including estimators
# - Pipelines provide convenience `fit`/`transform` that can be called for single inputs across multiple objecst at once
# - provide a single interface for grid search of multiple estimators at once
# - provide `operationalization` of text models by coupling a 