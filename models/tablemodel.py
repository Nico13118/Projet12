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


class ContractStatus(Base):
    __tablename__ = 'contractstatus'
    contract_status_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    contract_status_name: Mapped[str] = mapped_column(String(20), nullable=False)

    contractstatus_contract: Mapped[List['Contract']] = relationship(back_populates='contract_contractstatus')

    def __repr__(self) -> str:
        return f"Contract name={self.contract_status_name}"


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    role_name: Mapped[str] = mapped_column(String(3),
                                           nullable=False)  # nullable=False >> Le champ ne peut pas être vide
    # Role >> Collaborator : One-to-Many : Un rôle peut avoir plusieurs collaborateurs.
    collab: Mapped[List['Collaborator']] = relationship(back_populates='role')

    def __repr__(self) -> str:
        return f"<Role name={self.role_name}>"


class Collaborator(Base):
    __tablename__ = 'collaborator'
    collab_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    collab_name: Mapped[str] = mapped_column(String(100), nullable=False)
    collab_first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    collab_email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    collab_username: Mapped[str] = mapped_column(String(100), nullable=False)
    collab_password: Mapped[str] = mapped_column(String(100), nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'), nullable=False)
    #  Collaborator >> Role : Many-to-One : Chaque collaborateur ne peut avoir qu’un seul rôle.
    role: Mapped['Role'] = relationship(back_populates='collab')

    #  Collaborator >> Customer : One-to-Many : Un collaborateur peut avoir plusieurs clients
    collaborator_customer: Mapped[List['Customer']] = relationship(
        back_populates='customer_collaborator', cascade='all, delete', passive_deletes=True)

    #  Collaborator >> Contract : One-to-Many : Un collaborateur peut avoir plusieurs Contrats
    collaborator_contract: Mapped[List['Contract']] = relationship(back_populates='contract_collaborator',
                                                                   cascade='all, delete', passive_deletes=True)

    #  Collaborator >> Event : One-to-Many : Un collaborateur peut avoir plusieurs évènements
    collaborator_event: Mapped[List['Event']] = relationship(
        back_populates='event_collaborator', cascade='all, delete', passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Collaborator full_name={self.collab_name} {self.collab_first_name}>"


class Customer(Base):
    __tablename__ = 'customer'
    custom_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    custom_name: Mapped[str] = mapped_column(String(100))
    custom_first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    custom_email: Mapped[str] = mapped_column(String(100), nullable=False)
    custom_phone: Mapped[str] = mapped_column(String(20), nullable=False)
    custom_company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    custom_created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True),
                                                                   server_default=func.now(), nullable=False)
    custom_update_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                                  server_onupdate=func.now(), nullable=False)

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.collab_id', ondelete='SET NULL'),
                                                 nullable=True)
    #  Customer >> Collaborator : Many-to-One : Chaque Client ne peut avoir qu'un seul collaborateur
    customer_collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='collaborator_customer')

    #  Customer >> Contract : One-to-Many : Un client peut avoir plusieurs Contrats
    customer_contract: Mapped[List['Contract']] = relationship(back_populates='customer')

    #  Customer >> Event : One-to-Many : Un client peut avoir plusieurs évènements
    customer_event: Mapped[List['Event']] = relationship(back_populates='event_customer')

    def __repr__(self) -> str:
        return f"<Customer full_name={self.custom_name} {self.custom_first_name}"


class Contract(Base):
    __tablename__ = 'contract'
    contract_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    contract_description: Mapped[str] = mapped_column(String(500), nullable=True)
    contract_total_price: Mapped[int] = mapped_column(nullable=False)
    contract_amount_remaining: Mapped[int] = mapped_column(default=0, nullable=True)
    contract_created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    contract_status_id: Mapped[int] = mapped_column(ForeignKey('contractstatus.contract_status_id'), nullable=False,
                                                    default=2)
    contract_contractstatus: Mapped['ContractStatus'] = relationship(back_populates='contractstatus_contract')

    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.custom_id'), nullable=False)
    # Contract >> Customer : Many-to-One : Chaque contrat ne peut avoir qu'un seul client
    customer: Mapped['Customer'] = relationship(back_populates='customer_contract')

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.collab_id',
                                                            ondelete='SET NULL'), nullable=True)
    # Contract >> Collaborator : Many-to-One : Chaque contrat ne peut avoir qu'un seul collaborateur
    contract_collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='collaborator_contract')

    # Contract >> Event : Many-to-One : Chaque contrat ne peut avoir qu'un seul évènement
    contract_event: Mapped['Event'] = relationship(back_populates='event_contract')


class Event(Base):
    __tablename__ = 'event'
    event_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    event_date_start: Mapped[str] = mapped_column(String(30), nullable=False)
    event_date_end: Mapped[str] = mapped_column(String(30), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False)
    attendees: Mapped[str] = mapped_column(String(7), nullable=False)
    notes: Mapped[str] = mapped_column(String(500), nullable=False)

    collaborator_id: Mapped[int] = mapped_column(ForeignKey('collaborator.collab_id', ondelete='SET NULL'),
                                                 nullable=True)
    # Event >> Collaborator : Many-to-One : Chaque évènement ne peut avoir qu'un seul Collaborateur
    event_collaborator: Mapped[Optional['Collaborator']] = relationship(back_populates='collaborator_event')

    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.custom_id'), nullable=False)
    # Event >> Customer : Many-to-One : Chaque évènement ne peut avoir qu'un seul Client
    event_customer: Mapped['Customer'] = relationship(back_populates='customer_event')

    contract_id: Mapped[int] = mapped_column(ForeignKey('contract.contract_id'), nullable=False)
    # Event >> Contract : Many-to-One : Chaque évènement ne peut avoir qu'un seul Contrat
    event_contract: Mapped['Contract'] = relationship(back_populates='contract_event')
