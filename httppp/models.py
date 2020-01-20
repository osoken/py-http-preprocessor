# -*- coding: utf-8 -*-

from datetime import datetime
from .db import db


class RawData(db.Model):

    __tablename__ = 'raw_data'

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String, nullable=True)
    body = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


class Preprocessor(db.Model):
    __tablename__ = 'preprocessor'

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String, nullable=True)
    body = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


class ProcessedData(db.Model):
    __tablename__ = 'processed_data'

    id = db.Column(db.String(22), primary_key=True)
    raw_data_id = db.Column(
        db.String(64),
        db.ForeignKey('raw_data.id'),
        nullable=False
    )
    preprocessor_id = db.Column(
        db.String(64),
        db.ForeignKey('preprocessor.id'),
        nullable=False
    )
    body = db.Column(
        db.LargeBinary, nullable=False
    )
    __table_args__ = (
        db.Index(
            'processed_data_idx',
            'raw_data_id', 'preprocessor_id'
        ),)
