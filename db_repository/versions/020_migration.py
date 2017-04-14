from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
events = Table('events', pre_meta,
    Column('uid', INTEGER, primary_key=True, nullable=False),
    Column('autor_id', INTEGER),
    Column('description', VARCHAR(length=64)),
)

partipiant = Table('partipiant', pre_meta,
    Column('uid', INTEGER, primary_key=True, nullable=False),
    Column('event_id', INTEGER),
    Column('user_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['events'].drop()
    pre_meta.tables['partipiant'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['events'].create()
    pre_meta.tables['partipiant'].create()
