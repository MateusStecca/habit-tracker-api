from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db

# Cria as tabelas do banco automaticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Habit Tracker API")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao Habit Tracker API! O servidor está rodando perfeitamente."}

# Nova Rota: Criar um hábito
@app.post("/habits/", response_model=schemas.Habit)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    # Converte o dado que veio da internet para o modelo do banco de dados
    db_habit = models.HabitModel(
        title=habit.title, 
        description=habit.description, 
        is_active=habit.is_active
    )
    # Adiciona e salva no banco
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit) # Atualiza para pegar o ID que o banco gerou
    
    return db_habit
# Rota para listar todos os hábitos salvos
@app.get("/habits/", response_model=list[schemas.Habit])
def list_habits(db: Session = Depends(get_db)):
    # Busca todos os registros na tabela HabitModel
    habits = db.query(models.HabitModel).all()
    return habits

# Rota para deletar um hábito pelo ID
@app.delete("/habits/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    # Procura se o hábito existe no banco
    habit = db.query(models.HabitModel).filter(models.HabitModel.id == habit_id).first()
    
    if habit is None:
        return {"erro": "Hábito não encontrado"}
    
    # Deleta e confirma a exclusão no banco
    db.delete(habit)
    db.commit()
    return {"mensagem": "Hábito deletado com sucesso!"}