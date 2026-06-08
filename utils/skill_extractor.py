import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.blank("en")

ruler = nlp.add_pipe("entity_ruler")

patterns = [
    {"label": "SKILL", "pattern": "Python"},
    {"label": "SKILL", "pattern": "Machine Learning"},
    {"label": "SKILL", "pattern": "Deep Learning"},
    {"label": "SKILL", "pattern": "Artificial Intelligence"},
    {"label": "SKILL", "pattern": "SQL"},
    {"label": "SKILL", "pattern": "Power BI"},
    {"label": "SKILL", "pattern": "Tableau"},
    {"label": "SKILL", "pattern": "HTML"},
    {"label": "SKILL", "pattern": "CSS"},
    {"label": "SKILL", "pattern": "JavaScript"},
    {"label": "SKILL", "pattern": "React"},
    {"label": "SKILL", "pattern": "Node.js"},
    {"label": "SKILL", "pattern": "NLP"},
    {"label": "SKILL", "pattern": "RAG"},
    {"label": "SKILL", "pattern": "LangChain"},
]

ruler.add_patterns(patterns)


def extract_skills(text):
    doc = nlp(text)

    skills = []

    for ent in doc.ents:
        if ent.label_ == "SKILL":
            skills.append(ent.text)

    return list(set(skills))