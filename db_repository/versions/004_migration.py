from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
voc_folder = Table('voc_folder', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('autor', String(length=24)),
    Column('name_folder', String(length=24)),
)

voc_word = Table('voc_word', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('folder_id', String(length=24)),
    Column('eng', String(length=24)),
    Column('rus', String(length=24)),
    Column('desc', String(length=124)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['voc_folder'].create()
    post_meta.tables['voc_word'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['voc_folder'].drop()
    post_meta.tables['voc_word'].drop()
