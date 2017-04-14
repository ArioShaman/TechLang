from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
check_user = Table('check_user', pre_meta,
    Column('uid', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER),
    Column('check_unit', INTEGER),
)

check_unit_user = Table('check_unit_user', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('check_unit', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['check_user'].drop()
    post_meta.tables['check_unit_user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['check_user'].create()
    post_meta.tables['check_unit_user'].drop()
