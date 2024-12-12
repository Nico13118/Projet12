from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.sql import func
from typing import Optional, List
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
    role_name: Mapped[str] = mapped_column(String(3), nullable=False)  # nullable=False >> Le champ ne peut pas être vide
    # Role >> Collaborator : One-to-Many : Un rôle peut avoir plusieurs collaborateurs.
    collab: Mapped[List['Collaborator']] = relationship(back_populates='role')

    def __repr__(self) -> str:
        return f"<Role name={self.role_name}>"


class Collaborator(Base):
    __tablename__ = 'collaborator'
    collab_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'), nullable=False)
    #  Collaborator >> Role : Many-to-One : Chaque collaborateur ne peut avoir qu’un seul rôle.
    role: Mapped['Role'] = relationship(back_populates='collab')

    #  Collaborator >> Customer : One-to-Many : Un collaborateur peut avoir plusieurs clients
    custom: Mapped[List['Customer']] = relationship(
        back_populates='collaborator', cascade='all, delete', passive_deletes=True)

    #  Collaborator >> Contract : One-to-Many : Un collaborateur peut avoir plusieurs Contrats
    _contract: Mapped[List['Contract']] = relationship(
        back_populates='collaborator', cascade='all, delete', passive_deletes=True)

    #  Collaborator >> Event : One-to-Many : Un collaborateur peut avoir plusieurs évènements
    _event: Mapped[List['Event']] = relationship(
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
    update_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                           server_onupdate=func.now(), nullable=False)

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.collab_id', ondelete='SET NULL'),
                                                 nullable=True)
    #  Customer >> Collaborator : Many-to-One : Chaque Client ne peut avoir qu'un seul collaborateur
    collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='custom')

    #  Customer >> Contract : One-to-Many : Un client peut avoir plusieurs Contrats
    _contract: Mapped[List['Contract']] = relationship(back_populates='customer')

    #  Customer >> Event : One-to-Many : Un client peut avoir plusieurs évènements
    _event: Mapped[List['Event']] = relationship(back_populates='customer')

    def __repr__(self) -> str:
        return f"<Customer full_name={self.name} {self.first_name} " \
               f"Commercial: {self.collaborator.name} {self.collaborator.first_name}>"


class Contract(Base):
    __tablename__ = 'contract'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    contract_description: Mapped[str] = mapped_column(String(500), nullable=True)
    total_price: Mapped[int] = mapped_column(nullable=False)
    amount_remaining: Mapped[int] = mapped_column(default=0, nullable=True)
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    contract_signed: Mapped[str] = mapped_column(String(3), nullable=False, default="NO")

    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'), nullable=False)
    # Contract >> Customer : Many-to-One : Chaque contrat ne peut avoir qu'un seul client
    customer: Mapped['Customer'] = relationship(back_populates='_contract')

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.collab_id', ondelete='SET NULL'), nullable=True)
    # Contract >> Collaborator : Many-to-One : Chaque contrat ne peut avoir qu'un seul collaborateur
    collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='_contract')

    # Contract >> Event : Many-to-One : Chaque contrat ne peut avoir qu'un seul évènement
    _event: Mapped['Event'] = relationship(back_populates='contract')


class Event(Base):
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    event_date_start: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    event_date_end: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    location: Mapped[str] = mapped_column(String(200), nullable=False)
    attendees: Mapped[int] = mapped_column(String(7), nullable=False)
    notes: Mapped[str] = mapped_column(String(500), nullable=False)

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.collab_id', ondelete='SET NULL'),
                                                 nullable=True)
    # Event >> Collaborator : Many-to-One : Chaque évènement ne peut avoir qu'un seul Collaborateur
    collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='_event')

    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'), nullable=False)
    # Event >> Customer : Many-to-One : Chaque évènement ne peut avoir qu'un seul Client
    customer: Mapped['Customer'] = relationship(back_populates='_event')

    contract_id: Mapped[int] = mapped_column(ForeignKey('contract.id'), nullable=False)
    # Event >> Contract : Many-to-One : Chaque évènement ne peut avoir qu'un seul Contrat
    contract: Mapped['Contract'] = relationship(back_populates='_event')
