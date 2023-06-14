from fastapi import APIRouter

router = APIRouter()


@router.get('/generate_image')
def generate_image(prompt: str):
  return f"Prompt is {prompt}"