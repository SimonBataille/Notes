from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

articles = {
    1: {'nom' : 'Unite Centrale', 'prix' : 750},
    1: {'nom' : 'Ecran', 'prix' : 350}
}

class Article(BaseModel):
    nom: str
    prix: int

@app.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id: int):
    if article_id in articles:
        return articles[article_id]
    else:
        raise HTTPException(status_code=404, detail='Articles non trouve !')
    
@app.post("/articles/", response_model=Article)
async def create_article(article: Article):
    new_id = max(articles.keys()) + 1
    articles[new_id] = article.model_dump()
    return article