from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
videos = Table('videos', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('desc', String(length=124)),
    Column('link_video', String(length=124)),
    Column('cover', String(length=564)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['videos'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['videos'].drop()
