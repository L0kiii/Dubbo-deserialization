# Apache Dubbo Deserialization Vulnerability Research

This repository contains research materials, proof-of-concept code, and exploitation tools related to Apache Dubbo deserialization vulnerabilities, primarily focusing on CVE-2020-1948.

## Repository Structure

### Directories

- **Hessian-Deserialize-RCE-master**: Research and exploitation techniques for Hessian deserialization vulnerabilities in Dubbo
- **JNDI-Injection-Exploit-master**: JNDI injection exploitation framework for attacking Dubbo services
- **dubbo-dubbo-2.7.5**: Apache Dubbo 2.7.5 source code for vulnerability analysis
- **dubbo-exp-master**: Advanced exploitation framework for Dubbo vulnerabilities
- **dubbo-samples-master**: Sample Dubbo applications for testing and demonstration
- **marshalsec-master**: Tools for marshalling/unmarshalling vulnerability testing

### Files

- **dubboExp.py**: Python-based exploit script for CVE-2020-1948
- **dubboPoc.py**: Proof of concept script to verify vulnerability existence
- **payload.ser**: Serialized Java payload for exploitation
- **ysoserial.jar**: Java deserialization payload generation tool

## Vulnerability Overview

Apache Dubbo versions prior to 2.7.8, 2.6.9, and 2.5.10 are vulnerable to a remote code execution attack (CVE-2020-1948) due to insecure deserialization. The vulnerability affects the Dubbo Provider component, which uses Java native serialization without proper validation.

## Technical Details

This vulnerability can be exploited through multiple vectors:

1. **Hessian Deserialization**: Exploiting the Hessian serialization protocol implementation
2. **JNDI Injection**: Leveraging JNDI injection techniques to achieve remote code execution
3. **Java Serialization**: Using traditional Java deserialization attacks with gadget chains

## Usage

### Setup Vulnerable Environment

```bash
# Clone and build a vulnerable Dubbo version
cd dubbo-dubbo-2.7.5
mvn clean package
```

### Vulnerability Verification

```bash
# Run the proof of concept
python dubboPoc.py -t <target_ip> -p <target_port>
```

### Exploitation

```bash
# Run the exploit
python dubboExp.py -t <target_ip> -p <target_port> -c "command_to_execute"
```

### Custom Payload Generation

You can use ysoserial.jar to generate custom payloads:

```bash
java -jar ysoserial.jar CommonsCollections1 "command_to_execute" > payload.ser
```

## Mitigations

To protect against these vulnerabilities:

1. Upgrade to Apache Dubbo 2.7.8+, 2.6.9+, or 2.5.10+
2. Avoid using native Java serialization
3. Implement proper input validation and deserialization filtering
4. Consider using alternative serialization protocols with proper security controls

## References

- [CVE-2020-1948 Details](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1948)
- [Apache Dubbo Security Bulletin](https://github.com/apache/dubbo/security/advisories)
- [Java Deserialization Attacks and Defenses](https://snyk.io/blog/java-deserialization-attacks-guide/)
- [Understanding JNDI Injection](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf)

## Disclaimer

This repository is for security research and educational purposes only. The provided code and tools should only be used against systems you have permission to test. Any misuse of this information is not the responsibility of the repository owner.
