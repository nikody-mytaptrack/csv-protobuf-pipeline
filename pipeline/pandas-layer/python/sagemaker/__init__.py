# Copyright 2017-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from __future__ import absolute_import

from sagemaker import estimator  # noqa: F401
from sagemaker.amazon.kmeans import KMeans, KMeansModel, KMeansPredictor  # noqa: F401
from sagemaker.amazon.pca import PCA, PCAModel, PCAPredictor  # noqa: F401
from sagemaker.amazon.lda import LDA, LDAModel, LDAPredictor  # noqa: F401
from sagemaker.amazon.linear_learner import LinearLearner, LinearLearnerModel, LinearLearnerPredictor  # noqa: F401
from sagemaker.amazon.factorization_machines import FactorizationMachines, FactorizationMachinesModel  # noqa: F401
from sagemaker.amazon.factorization_machines import FactorizationMachinesPredictor  # noqa: F401
from sagemaker.amazon.ntm import NTM, NTMModel, NTMPredictor  # noqa: F401
from sagemaker.amazon.randomcutforest import (RandomCutForest, RandomCutForestModel,  # noqa: F401
                                              RandomCutForestPredictor)
from sagemaker.amazon.knn import KNN, KNNModel, KNNPredictor  # noqa: F401
from sagemaker.amazon.object2vec import Object2Vec, Object2VecModel  # noqa: F401
from sagemaker.amazon.ipinsights import IPInsights, IPInsightsModel, IPInsightsPredictor  # noqa: F401

from sagemaker.analytics import TrainingJobAnalytics, HyperparameterTuningJobAnalytics  # noqa: F401
from sagemaker.local.local_session import LocalSession  # noqa: F401

from sagemaker.model import Model  # noqa: F401
from sagemaker.predictor import RealTimePredictor  # noqa: F401
from sagemaker.session import Session  # noqa: F401
from sagemaker.session import container_def  # noqa: F401
from sagemaker.session import production_variant  # noqa: F401
from sagemaker.session import s3_input  # noqa: F401
from sagemaker.session import get_execution_role  # noqa: F401

__version__ = '1.15.0'
