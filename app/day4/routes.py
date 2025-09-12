from fastapi import APIRouter, HTTPException
from app.day4.models import Note

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

notes_db: list[dict] = []

@router.post("/create_note",response_model=Note)
async def create_note(note: Note):
    notes_db.append(note.model_dump())
    return note

@router.get("/", response_model=list[Note])
async def list_notes():
    return notes_db

@router.get("/{note_id}", response_model=Note)
async def get_note(note_id: int):
    if note_id < 0 or note_id >= len(notes_db):
        raise HTTPException(status_code=404, detail="Note not found")
    return notes_db[note_id]





