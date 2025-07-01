from sqlalchemy import ForeignKey
from sqlalchemy.types import String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from typing import Optional, List



class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'user'

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(primary_key=True)
    phonenumber: ...
    username: Mapped[str]


class Battle(Base):
    ...






class Deck(Base):
    __tablename__ = 'deck'
 
    id           : Mapped[int]     = mapped_column(primary_key=True, autoincrement=True)
    hash         : Mapped[String]  = mapped_column(unique=True, nullable=False)
    game         : Mapped[int]     = mapped_column(ForeignKey("game.id"))
    cards_amount : Mapped[int]     = mapped_column(nullable=False)
    has_jokers   : Mapped[Boolean] = mapped_column(nullable=False)