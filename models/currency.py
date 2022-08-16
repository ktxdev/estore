from sqlalchemy import Column, Integer, String, Boolean, Float

from database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    code = Column(String(16))
    default = Column(Boolean(create_constraint=False), default=False)
    rateToDefault = Column(Float, default=1.0)

