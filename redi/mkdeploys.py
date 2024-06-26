import sys, os
from subprocess import Popen, PIPE
sys.path.append(os.getcwd()+"/..")
from utils import DeploymentWriter

class RediDeploymentWriter(DeploymentWriter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _replace_placeholders(self, config, name, text):
        text = text.replace("SITE_PLACEHOLDER", self._get_site_name(config))
        text = text.replace("NODE_PLACEHOLDER", config["node"])
        text = text.replace("NAME_PLACEHOLDER", name)
        text = text.replace("INTF_PLACEHOLDER", config["interface"])
        text = text.replace("MAIN_PORT_PLACEHOLDER", config["main_port"])
        text = text.replace("REDI_PORT_PLACEHOLDER", config["redi_port"])
        text = text.replace("IPV6_PLACEHOLDER", config["ipv6"])
        text = text.replace("MULTUS_PLACEHOLDER", config["multus"])
        text = text.replace("GATEWAY_PLACEHOLDER", config["gateway"])
        text = text.replace("MAC_PLACEHOLDER", config["mac"])
        text = text.replace("CERTS_PLACEHOLDER", config["certs"])
        return text

    def _get_deployment_name(self, config):
        ipv6_last4 = config["ipv6"].split(":")[-1]
        ipv6_subnet = config["ipv6"].split(":")[-3]
        return f"{self.app_name}-{ipv6_subnet}-{ipv6_last4}"

    def _get_site_name(self, config):
        ipv6_last4 = config["ipv6"].split(":")[-1]
        return f"RUCIO_SENSE_REDI_{ipv6_last4}_{config['main_port']}_{config['redi_port']}"

    def make_certs(self):
        if len(self._get_deployments()) == 0:
            print("WARNING: No certs made; run write() first!")
            return
        for config in self.configs:
            base_dir = f"{os.getcwd()}/{self.deployment_dir}/{self._get_deployment_name(config)}"
            cmd = f"../certs/generate.sh {config['ipv6']} {base_dir}"
            Popen(cmd.split(), cwd="../certs", stdout=PIPE).communicate()

if __name__ == "__main__":
    redi_configs = [
        {
            "node": "k8s-gen5-01.sdsc.optiputer.net", 
            "ipv6": "2001:48d0:3001:111::800",
            "multus": "multus111",
            "mac": "56:25:24:23:4f:49",
            "gateway": "2001:48d0:3001:111::1",
            "main_port": "1094",
            "interface": "enp1s0f1np1",
            "redi_port": "1213",
            "certs": "certs-redi"
        },
        {
            "node": "k8s-gen5-02.sdsc.optiputer.net", 
            "ipv6": "2001:48d0:3001:112::800",
            "multus": "multus112",
            "mac": "06:a5:af:ef:3c:de",
            "gateway": "2001:48d0:3001:112::1",
            "main_port": "1094",
            "interface": "enp1s0f1np1",
            "redi_port": "1213",
            "certs": "certs-redi"
        },
        {
            "node": "k8s-gen5-01.sdsc.optiputer.net", 
            "ipv6": "2001:48d0:3001:113::800",
            "multus": "multus113",
            "mac": "56:25:24:23:4f:49",
            "gateway": "2001:48d0:3001:113::1",
            "main_port": "1094",
            "interface": "enp1s0f1np1",
            "redi_port": "1213",
            "certs": "certs-redi"
        },
        {
            "node": "k8s-gen5-02.sdsc.optiputer.net", 
            "ipv6": "2001:48d0:3001:114::800",
            "multus": "multus114",
            "mac": "06:a5:af:ef:3c:de",
            "gateway": "2001:48d0:3001:114::1",
            "main_port": "1094",
            "interface": "enp1s0f1np1",
            "redi_port": "1213",
            "certs": "certs-redi"
        },
    ]
    deployment_writer = RediDeploymentWriter(
        base_dir="./", 
        template_dir="templates", 
        app_name="rucio-sense-redi", 
        configs=redi_configs
    )
    deployment_writer.write()
