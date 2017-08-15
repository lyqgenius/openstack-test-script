import nova.context as nova_context
import drsstack.rs.conf
import drsstack.openstack.openstack_utils as openstack_utils
from novaclient import service_catalog

CONF = drsstack.rs.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
CONF(argv, default_config_files=default_config_files)
group_name = drsstack.rs.conf.client.CLIENT_GROUP_NAME
auth_plugin = openstack_utils.create_auth_plugin(CONF, group_name)
kwargs = {'auth': auth_plugin}
client_session = openstack_utils.create_client_session(CONF, group_name,
                                                       **kwargs)
project_name = CONF[group_name].project_name
username = CONF[group_name].username
user_domain_name = CONF[group_name].user_domain_name
p_domain_name = CONF[group_name].project_domain_name
access_info = auth_plugin.get_auth_ref(client_session)
auth_token = access_info.auth_token
catalog = getattr(access_info.service_catalog, 'catalog', None)

# context = nova_context.RequestContext(user_name=username,
#                                       project_name=project_name,
#                                       user_domain_name=user_domain_name,
#                                       project_domain_name=p_domain_name,
#                                       is_admin=True,
#                                       read_deleted='no',
#                                       user_auth_plugin=auth_plugin,
#                                       auth_token=auth_token,
#                                       service_catalog=catalog)

v2_services = []
for v3_service in catalog:
    v2_service = {'type': v3_service['type']}
    try:
        v2_service['name'] = v3_service['name']
    except KeyError:  # nosec
        pass

    regions = {}
    for v3_endpoint in v3_service.get('endpoints', []):
        region_name = v3_endpoint.get('region')
        try:
            region = regions[region_name]
        except KeyError:
            region = {'region': region_name} if region_name else {}
            regions[region_name] = region

        interface_name = v3_endpoint['interface'].lower() + 'URL'
        region[interface_name] = v3_endpoint['url']

    v2_service['endpoints'] = list(regions.values())
    v2_services.append(v2_service)
catalog = v2_services
context = nova_context.RequestContext(user_name=username,
                                      project_name=project_name,
                                      user_domain_name=user_domain_name,
                                      project_domain_name=p_domain_name,
                                      is_admin=True,
                                      read_deleted='no',
                                      auth_token=auth_token,
                                      service_catalog=catalog)
auth = context.get_auth_plugin()
import pdb;

pdb.set_trace()
auth.get_endpoint(client_session, service_type='volumev2')
