#!/usr/bin/python3

import xml.etree.ElementTree as ET
import hashlib
import time
from datetime import datetime

def calculate_hashes(filename):
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            md5_hash.update(chunk)
            sha1_hash.update(chunk)
    
    return md5_hash.hexdigest(), sha1_hash.hexdigest()

def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    hosts = root.findall('.//host')
    
    num_hosts_on = 0
    num_hosts_off = 0
    num_ports_22 = 0
    num_ports_53 = 0
    num_ports_80 = 0
    num_ports_443 = 0
    num_domain_names = 0
    http_servers = set()
    apache_count = 0
    dionaea_count = 0
    nginx_count = 0
    
    for host in hosts:
        status = host.find('status')
        if status is not None:
            state = status.get('state')
            if state == 'up':
                num_hosts_on += 1
            elif state == 'down':
                num_hosts_off += 1
        
        ports = host.find('ports')
        if ports is not None:
            for port in ports:
                port_number = port.get('portid')
                if port_number == '22':
                    num_ports_22 += 1
                elif port_number == '53':
                    num_ports_53 += 1
                elif port_number == '80':
                    num_ports_80 += 1
                elif port_number == '443':
                    num_ports_443 += 1
        
        hostnames = host.find('hostnames')
        if hostnames is not None:
            num_domain_names += len(hostnames.findall('hostname'))
        
        os = host.find('os')
        if os is not None:
            if 'Apache' in os.text:
                apache_count += 1
            if 'Dionaea' in os.text:
                dionaea_count += 1
            if 'Nginx' in os.text:
                nginx_count += 1

        http_servers.add(os.text if os is not None else 'Unknown')
    
    return {
        'num_hosts_on': num_hosts_on,
        'num_hosts_off': num_hosts_off,
        'num_ports_22': num_ports_22,
        'num_ports_53': num_ports_53,
        'num_ports_80': num_ports_80,
        'num_ports_443': num_ports_443,
        'num_domain_names': num_domain_names,
        'http_servers': http_servers,
        'apache_count': apache_count,
        'dionaea_count': dionaea_count,
        'nginx_count': nginx_count
    }

def report(filename):
    start_time = time.time()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    xml_file = 'nmap.xml'
    
    md5_hash, sha1_hash = calculate_hashes(xml_file)
    
    stats = parse_xml(xml_file)
    
    report_content = f"""
    Informe Generado: {current_time}
    Hora de Ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    MD5 del archivo XML: {md5_hash}
    SHA1 del archivo XML: {sha1_hash}
    Cantidad de hosts prendidos: {stats['num_hosts_on']}
    Cantidad de hosts apagados: {stats['num_hosts_off']}
    Cantidad de hosts con puerto 22 abierto: {stats['num_ports_22']}
    Cantidad de hosts con puerto 53 abierto: {stats['num_ports_53']}
    Cantidad de hosts con puerto 80 abierto: {stats['num_ports_80']}
    Cantidad de hosts con puerto 443 abierto: {stats['num_ports_443']}
    Cantidad de hosts que tienen nombre de dominio: {stats['num_domain_names']}
    Servidores HTTP usados: {', '.join(stats['http_servers'])}
    Cuántos usan Apache: {stats['apache_count']}
    Cuántos honeypots (Dionaea): {stats['dionaea_count']}
    Cuántos usan Nginx: {stats['nginx_count']}
    """
    
    with open('informe.txt', 'w') as f:
        f.write(report_content)
    
    print(report_content)

if __name__ == '__main__':
    report('data.xml')


