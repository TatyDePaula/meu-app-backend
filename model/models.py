from sqlalchemy import Boolean, Column, String, Integer, DateTime, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Union

from model import Base


class Convidado(Base):
    __tablename__ = 'convidado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_convidado = Column(Integer, nullable=False)
    nome = Column(String(255), nullable=False)
    numero_telefone = Column(String(20), nullable=False)

    def __init__(self, numero_convidado: int, nome: str, numero_telefone: str):
        self.numero_convidado = numero_convidado
        self.nome = nome
        self.numero_telefone = numero_telefone
