from fastapi import FastAPI
from routes import A_bubble_sort
from routes import B_selection_sort
from routes import C_insertion_sort

app = FastAPI()
app.include_router(A_bubble_sort.router, prefix="")
app.include_router(B_selection_sort.router, prefix="")
app.include_router(C_insertion_sort.router, prefix="")
