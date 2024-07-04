from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '489e0a38d6bf'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('now()'))

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Float(),
               existing_nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('now()'))
        batch_op.alter_column('rating',
               existing_type=sa.Float(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)

    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###
