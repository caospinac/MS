import sqlalchemy as sa
from . import Model


class User(Model):

    __tablename__ = 'users'
    __table_args__ = (
        sa.UniqueConstraint('organization_id', 'email',
                         name='_organization_email_uc'),
    )
    _repr_hide = ['password']

    external_id = sa.Column(sa.String, nullable=False)
    status = sa.Column(sa.Enum('active', 'inactive'),
                    nullable=False, default='inactive')
    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    birthdate = sa.Column(sa.DateTime)
    phone_number = sa.Column(sa.String)
    gender = sa.Column(sa.Enum('f' 'm'))
    avatar = sa.Column(sa.String)
