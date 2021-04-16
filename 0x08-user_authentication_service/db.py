#!/usr/bin/env python3
"""te, find and update user
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class definition"""

    def __init__(self):
        """Constructor method"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Session maker"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add user in database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **filters) -> User:
        """Returns the  matches first row"""
        if not User.__dict__.get(*filters):
            raise InvalidRequestError
        query = self._session.query(User).filter_by(**filters)
        if not query.first():
            raise NoResultFound
        return query.first()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user that passes by the args"""
        user_to_update = self.find_user_by(id=user_id)

        for key, val in kwargs.items():
            if hasattr(user_to_update, key):
                setattr(user_to_update, key, val)
            else:
                raise ValueError

        self._session.commit()
