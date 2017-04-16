from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('uid', INTEGER, primary_key=True, nullable=False),
    Column('autor', VARCHAR(length=24)),
    Column('title', VARCHAR(length=24)),
    Column('desk', VARCHAR(length=124)),
    Column('cover', VARCHAR(length=564)),
    Column('article', VARCHAR(length=560)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['article'].drop()
    pre_meta.tables['post'].columns['autor'].drop()
    pre_meta.tables['post'].columns['cover'].drop()
    pre_meta.tables['post'].columns['desk'].drop()
    pre_meta.tables['post'].columns['title'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['article'].create()
    pre_meta.tables['post'].columns['autor'].create()
    pre_meta.tables['post'].columns['cover'].create()
    pre_meta.tables['post'].columns['desk'].create()
    pre_meta.tables['post'].columns['title'].create()
