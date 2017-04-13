from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
admin = Table('admin', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('Lastname', String(length=24)),
    Column('Firstname', String(length=24)),
    Column('email', String(length=120)),
    Column('town', String(length=40)),
    Column('age', Integer),
    Column('role', SmallInteger, default=ColumnDefault(1)),
    Column('password', String(length=64), default=ColumnDefault('admin')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['admin'].columns['age'].create()
    post_meta.tables['admin'].columns['town'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['admin'].columns['age'].drop()
    post_meta.tables['admin'].columns['town'].drop()
