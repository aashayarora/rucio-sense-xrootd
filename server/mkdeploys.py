import sys, os
import random
from subprocess import Popen, PIPE
sys.path.append(os.getcwd()+"/..")
from utils import DeploymentWriter

class ServerDeploymentWriter(DeploymentWriter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _replace_placeholders(self, config, name, text):
        text = text.replace("SITE_PLACEHOLDER", self._get_site_name(config))
        text = text.replace("NODE_PLACEHOLDER", config["node"])
        text = text.replace("NAME_PLACEHOLDER", name)
        text = text.replace("REDI_IPV6_PLACEHOLDER", config["redi_ipv6"])
        text = text.replace("REDI_PORT_PLACEHOLDER", config["redi_port"])
        text = text.replace("INTF_PLACEHOLDER", config["interface"])
        text = text.replace("PORT_PLACEHOLDER", config["port"])
        text = text.replace("IPV6_PLACEHOLDER", config["ipv6"])
        text = text.replace("MULTUS_PLACEHOLDER", config["multus"])
        text = text.replace("GATEWAY_PLACEHOLDER", config["gateway"])
        text = text.replace("MAC_PLACEHOLDER", config["mac"])
        text = text.replace("CERTS_PLACEHOLDER", config["certs"])
        return text

    def _get_deployment_name(self, config):
        N = config["node"].split(".")[0]
        return f"{self.app_name}-{N}-{config['multus'][-3:]}-{config['port'].replace('.', '-')}"

    def _get_site_name(self, config):
        ipv6_last4 = config["ipv6"].split(":")[-1]
        return f"RUCIO_SENSE_SERVER_{ipv6_last4}_{config['port']}"

    def make_certs(self):
        if len(self._get_deployments()) == 0:
            print("WARNING: No certs made; run write() first!")
            return
        for config in self.configs:
            base_dir = f"{os.getcwd()}/{self.deployment_dir}/{self._get_deployment_name(config)}"
            cmd = f"../certs/generate.sh {config['ipv6']} {base_dir}"
            Popen(cmd.split(), cwd="../certs", stdout=PIPE).communicate()

def make_k8s_gen4_servers():
    server_configs = [
        # Cluster 2
        {
            "node": "k8s-gen4-01.sdsc.optiputer.net", 
            "ipv6": "2001:48d0:3001:111::400",
            "multus": "multus111",
            "mac": "4a:63:d1:f8:02:56",
            "gateway": "2001:48d0:3001:111::1",
            "port": "1094",
            "certs": "certs-400",
            "interface": "enp1s0f1np1",
            "redi_ipv6": "2001:48d0:3001:111::800",
            "redi_port": "1213",
        }, 
#        {
#            "node": "k8s-gen4-02.sdsc.optiputer.net", 
#            "ipv6": "2001:48d0:3001:111::500",
#            "multus": "multus111-1",
#            "mac": "be:17:3d:9c:45:df",
#            "gateway": "2001:48d0:3001:111::1",
#            "port": "1094",
#            "certs": "certs-500",
#            "interface": "enp1s0f1np1",
#            "redi_ipv6": "2001:48d0:3001:111::800",
#            "redi_port": "1213",
#        }, 
#        {
#            "node": "k8s-gen4-02.sdsc.optiputer.net", 
#            "ipv6": "2001:48d0:3001:111::700",
#            "certs": "certs-700",
#            "multus": "multus111-3",
#            "mac": "76:22:27:ed:2a:f7",
#            "gateway": "2001:48d0:3001:111::1",
#            "port": "1094",
#            "interface": "enp1s0f1np1",
#            "redi_ipv6": "2001:48d0:3001:111::800",
#            "redi_port": "1213",
#        }, 
#        {
#            "node": "k8s-gen4-02.sdsc.optiputer.net", 
#            "ipv6": "2001:48d0:3001:111::600",
#            "certs": "certs-600",
#            "multus": "multus111-4",
#            "mac": "ce:9d:1c:86:79:60",
#            "gateway": "2001:48d0:3001:111::1",
#            "port": "1094",
#            "interface": "enp1s0f1np1",
#            "redi_ipv6": "2001:48d0:3001:111::800",
#            "redi_port": "1213",
#        }, 
        {
            "node": "k8s-gen4-02.sdsc.optiputer.net", 
            "ipv6": "2001:48d0:3001:112::400",
            "multus": "multus112",
            "mac": "e6:ba:06:08:4d:13",
            "gateway": "2001:48d0:3001:112::1",
            "port": "1094",
            "certs": "certs-400",
            "interface": "enp1s0f1np1",
            "redi_ipv6": "2001:48d0:3001:112::800",
            "redi_port": "1213",
        }, 
#        {
#            "node": "k8s-gen4-01.sdsc.optiputer.net", 
#            "ipv6": "2001:48d0:3001:112::500",
#            "multus": "multus112-1",
#            "mac": "be:c5:c0:e7:a1:d2",
#            "gateway": "2001:48d0:3001:112::1",
#            "port": "1094",
#            "certs": "certs-500",
#            "interface": "enp1s0f1np1",
#            "redi_ipv6": "2001:48d0:3001:112::800",
#            "redi_port": "1213",
#        }, 
#        {
#            "node": "k8s-gen4-01.sdsc.optiputer.net", 
#            "ipv6": "2001:48d0:3001:112::600",
#            "certs": "certs-600",
#            "multus": "multus112-2",
#            "mac": "8a:d5:97:75:18:91",
#            "gateway": "2001:48d0:3001:112::1",
#            "port": "1094",
#            "interface": "enp1s0f1np1",
#            "redi_ipv6": "2001:48d0:3001:112::800",
#            "redi_port": "1213",
#        }, 
#        {
#            "node": "k8s-gen4-01.sdsc.optiputer.net", 
#            "ipv6": "2001:48d0:3001:112::700",
#            "certs": "certs-700",
#            "multus": "multus112-3",
#            "mac": "9e:b7:d5:eb:f1:0f",
#            "gateway": "2001:48d0:3001:112::1",
#            "port": "1094",
#            "interface": "enp1s0f1np1",
#            "redi_ipv6": "2001:48d0:3001:112::800",
#            "redi_port": "1213",
#        }, 
    ]
    deployment_writer = ServerDeploymentWriter(
        base_dir="./", 
        template_dir="templates", 
        app_name="rucio-sense-server", 
        configs=server_configs
    )
    deployment_writer.write()

if __name__ == "__main__":
     make_k8s_gen4_servers()
