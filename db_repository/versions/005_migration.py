from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
voc_word = Table('voc_word', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('folder_id', String(length=24)),
    Column('eng', String(length=24)),
    Column('rus', String(length=24)),
    Column('desc', String(length=124)),
    Column('link_cover', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['voc_word'].columns['link_cover'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['voc_word'].columns['link_cover'].drop()
