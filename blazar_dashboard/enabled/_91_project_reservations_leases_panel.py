#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'leases'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'reservations'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'blazar_dashboard.content.leases.panel.Leases'

ADD_SCSS_FILES = [
    'leases/scss/calendar.scss',
    'leases/scss/detail_overview.scss',
    'leases/scss/widgets.scss',
]

ADD_JS_FILES = [
    'leases/js/calendar/lease_chart.js',
    'leases/js/vendor/apexcharts.min.js',
    'leases/js/create_lease/extra_capability_widget.js',
    'leases/js/create_lease/workflow.js',
]
