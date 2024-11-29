from sqlalchemy import ForeignKey, String, DateTime, Enum
from sqlalchemy.sql import func
from typing import Optional, Literal
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(3), nullable=False)  # nullable=False >> Le champ ne peut pas être vide
    # Role à une relation avec Collaborator
    collab: Mapped[Optional['Collaborator']] = relationship(back_populates='role')

    def __repr__(self) -> str:
        return f"<Role name={self.name}>"


class Collaborator(Base):
    __tablename__ = 'collaborator'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    role_id: Mapped[str] = mapped_column(ForeignKey('role.id'), nullable=False)
    #  Collaborator à une relation avec Role
    role: Mapped[Optional['Role']] = relationship(back_populates='collab')

    #  Collaborator à une relation avec Customer
    custom: Mapped[Optional['Customer']] = relationship(
        back_populates='collaborator', cascade='all, delete', passive_deletes=True)
    #  Collaborator à une relation avec Contract
    _contract: Mapped[Optional['Contract']] = relationship(
        back_populates='collaborator', cascade='all, delete', passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Collaborator full_name={self.name} {self.first_name}>"


class Customer(Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True),
                                                            server_default=func.now(), nullable=False)
    update_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                  server_onupdate=func.now(), nullable=False)

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.id', ondelete='SET NULL'), nullable=True)
    #  Customer à une relation avec Collaborator
    collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='custom')

    #  Customer à une relation avec Contract
    _contract: Mapped[Optional['Contract']] = relationship(back_populates='customer')

    def __repr__(self) -> str:
        return f"<Customer full_name={self.name} {self.first_name}"
        # f"Commercial: {self.collaborator.name} {self.collaborator.first_name}>"


class Contract(Base):
    __tablename__ = 'contract'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    contract_description: Mapped[str] = mapped_column(String(500), nullable=True)
    total_price: Mapped[int] = mapped_column(String(6), nullable=False)
    amount_remaining: Mapped[int] = mapped_column(String(6))
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    contract_signed: Mapped[str] = mapped_column(String(3), nullable=False, default="NO")

    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'), nullable=False)
    # Contract a une relation avec Customer
    customer: Mapped[Optional['Customer']] = relationship(back_populates='_contract')

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.id', ondelete='SET NULL'), nullable=True)
    # Contract a une relation avec Collaborator
    collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='_contract')
