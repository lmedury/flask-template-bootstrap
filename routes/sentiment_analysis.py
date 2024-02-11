from flask import Blueprint, render_template, request, jsonify, Response
from datetime import datetime
import zipfile, os, io, csv
import pandas as pd
import numpy as np

sentiment_analysis_router = Blueprint('sentiment-analysis', __name__)

@sentiment_analysis_router.route('/', methods=['GET'])
def saturation_reporting_template():
    return render_template('sentiment-analysis.html')