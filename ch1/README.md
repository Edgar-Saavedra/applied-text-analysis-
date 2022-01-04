Data science a mix of professions. Statistician, computer scientis, domain expert. Data scientists bridge work done in an academic context. Data science workflow not always compatible with Software Development practices.

Data Science Team -> Managment -> Tech Lead -> Dev Team -> product

Important to know how to build a large corpus, how to transform raw documents into usable data.

## Language Aware Data Products
Drive their value from data and generate new data in return.
No only reponsive to human input can adapt to change.

Example: Yelp insights. Uses sentiment analysis and significant collocation (words that tend to appear together). It uses a **domain specific corpus**. Automatic indentification of significant sentences.

Example: "suggested tag" tags indentify properties of the content they describe.

## Data product pipeline
Itterative process consistin of 2 phases : build and deploy.
- Build phase: data is ingested and wrangled into a form that allows models to be fit and experiment on.
- Deploy phase: models are selected and then used to make estimations or predictions.
- Interaction
  - Feedbac -> Ingestion
- Data
  - Wrangling
  - API
- Storage
  - Normalization
  - Model selection & Monitoring
- Computation
  - Feature analysis/model builds
  - Cros validation.
TL;DR: 
Build phase ingests data, wrangles it to a form that allows model to be fit and experiment.
Deploy phase - takes selected models and uses it to make estimates and predictsions.


### Models 
Relationship of variables to the target. An instance of features, algorithm and hyperparameters.
Fitted models ia s model form that has been fit to a specific set of training data and can make predictions.

We need to change how we see language and see it a numberic data.

### Language as data
Language is *unstructured* and governed by lingustic properties.
**Structured or Semistructured** data includes fiels or markup that enable it to be easily parsed by a computer.

Supervised learning is usually implement in text analysis.

**corpora** our training data

We assume text is predicatable.

- Take **tokens** strings of data, give a context and define a **constrained numeric decision space** on which models can compute.

## STEPS
1. Identify features of data. 
2. Context modifies, interpretation
3. Create a the traditional **bag-of-words** model

