from fastapi import FastAPI
from routers.blog import router as blog_router
from routers.auth import router as auth_router
from meta_tags .meta_tags import tags_metadata

from database.database import initiate_database

app = FastAPI(
              title="Blog Api ",
              description="this is a blog app with minimal usage of authentications and post managing",
              version="0.0.1",
              terms_of_service="https://ecample.com/terms",
              contact={
                  "name": "Shahram Samar",
                  "url":"https://shahramsamar.github.io/",
                  "email": "shahramsamar2010@gmail.com",
              },
              license_info={"name":"MIT"},
              openapi_tags=tags_metadata,
              docs_url="/",
            )




app.include_router(blog_router)
app.include_router(auth_router)
