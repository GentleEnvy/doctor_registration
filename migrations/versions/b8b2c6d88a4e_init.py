"""init

Revision ID: b8b2c6d88a4e
Revises: 
Create Date: 2021-07-15 23:37:00.697168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b2c6d88a4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('specialty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_specialty'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('mid_name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name=op.f('fk_admin_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_admin'))
    )
    op.create_table('doctor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specialty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name=op.f('fk_doctor_id_user')),
    sa.ForeignKeyConstraint(['specialty_id'], ['specialty.id'], name=op.f('fk_doctor_specialty_id_specialty')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_doctor'))
    )
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name=op.f('fk_patient_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_patient'))
    )
    op.create_table('record_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('weekday', sa.Integer(), nullable=False),
    sa.Column('start', sa.Time(), nullable=False),
    sa.Column('end', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], name=op.f('fk_record_time_doctor_id_doctor')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_record_time'))
    )
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('record_time_id', sa.Integer(), nullable=True),
    sa.Column('is_served', sa.Boolean(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], name=op.f('fk_appointment_patient_id_patient')),
    sa.ForeignKeyConstraint(['record_time_id'], ['record_time.id'], name=op.f('fk_appointment_record_time_id_record_time')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_appointment'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    op.drop_table('record_time')
    op.drop_table('patient')
    op.drop_table('doctor')
    op.drop_table('admin')
    op.drop_table('user')
    op.drop_table('specialty')
    # ### end Alembic commands ###
