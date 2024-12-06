from fastapi import FastAPI, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal, Usuario


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/usuario/")
def create_usuario(
    nombre: str = Form(...),
    apellido: str = Form(...),
    correo: str = Form(...),
    contraseña: str = Form(...),
    perfil: int = Form(...),
    rol: str = Form(...),
    db: Session = Depends(get_db),
):
    # Verificar si el correo ya está registrado
    usuario_existente = db.query(Usuario).filter(Usuario.Correo == correo).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")


    nuevo_usuario = Usuario(
        Nombre=nombre,
        Apellido=apellido,
        Correo=correo,
        Contraseña=contraseña,
        Id_Perfil=perfil,
        Rol=rol
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)


    return {"mensaje": "Usuario creado con éxito", "usuario": nuevo_usuario}