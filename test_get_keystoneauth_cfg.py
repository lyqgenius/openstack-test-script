from keystoneauth1 import loading as ks_loading
from oslo_config import cfg

opts = ks_loading.get_session_conf_options() + ks_loading.get_auth_common_conf_options() +ks_loading.get_auth_plugin_conf_options('password') +ks_loading.get_auth_plugin_conf_options('v2password') +ks_loading.get_auth_plugin_conf_options('v3password')

for opt in opts:
    print opt.dest