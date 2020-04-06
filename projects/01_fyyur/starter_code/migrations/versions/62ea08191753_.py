"""empty message

Revision ID: 62ea08191753
Revises: 69712e0b0424
Create Date: 2020-04-06 03:47:34.135316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62ea08191753'
down_revision = '69712e0b0424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('artist', sa.Column('artist_image_link', sa.String(length=500), nullable=True))
    op.add_column('artist', sa.Column('num_upcoming_shows', sa.Integer(), nullable=True))
    op.add_column('artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('artist', 'image_link')
    op.add_column('venue', sa.Column('genres', sa.String(), nullable=True))
    op.add_column('venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    op.add_column('venue', sa.Column('venue_image_link', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'website_link')
    op.drop_column('venue', 'venue_image_link')
    op.drop_column('venue', 'seeking_talent')
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'genres')
    op.add_column('artist', sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_column('artist', 'website_link')
    op.drop_column('artist', 'seeking_venue')
    op.drop_column('artist', 'seeking_description')
    op.drop_column('artist', 'num_upcoming_shows')
    op.drop_column('artist', 'artist_image_link')
    op.drop_table('show')
    # ### end Alembic commands ###
