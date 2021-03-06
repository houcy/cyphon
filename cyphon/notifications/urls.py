# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Urls for push notifications.
"""

# third party
from django.conf.urls import url

# local
from . import views


urlpatterns = [
	url(r'^subscribe/$', views.SubscribeView.as_view(), 
		name='notifications_subscribe'),
	url(r'test/$', views.TestNotifications.as_view(), name='notifications_test'),
	url(r'^$', views.NotificationView.as_view(), name='notifications_get')
]

