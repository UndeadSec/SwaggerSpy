<p align="center">
<img src="https://raw.githubusercontent.com/UndeadSec/SwaggerSpy/main/static/logo.png"/>
</p>

# SwaggerSpy

## Overview

SwaggerSpy is a tool designed for automated Open Source Intelligence (OSINT) on SwaggerHub. This project aims to streamline the process of gathering intelligence from APIs documented on SwaggerHub, providing valuable insights for security researchers, developers, and IT professionals.

<p align="center">
<img src="https://raw.githubusercontent.com/UndeadSec/SwaggerSpy/main/static/sc.png"/>
</p>

### What is Swagger?

Swagger is an open-source framework that allows developers to design, build, document, and consume RESTful web services. It simplifies API development by providing a standard way to describe REST APIs using a JSON or YAML format. Swagger enables developers to create interactive documentation for their APIs, making it easier for both developers and non-developers to understand and use the API.

### About SwaggerHub

SwaggerHub is a collaborative platform for designing, building, and managing APIs using the Swagger framework. It offers a centralized repository for API documentation, version control, and collaboration among team members. SwaggerHub simplifies the API development lifecycle by providing a unified platform for API design and testing.

### Why OSINT on SwaggerHub?

Performing OSINT on SwaggerHub is crucial because developers, in their pursuit of efficient API documentation and sharing, may inadvertently expose sensitive information. Here are key reasons why OSINT on SwaggerHub is valuable:

1. **Developer Oversights:** Developers might unintentionally include secrets, credentials, or sensitive information in API documentation on SwaggerHub. These oversights can lead to security vulnerabilities and unauthorized access if not identified and addressed promptly.

2. **Security Best Practices:** OSINT on SwaggerHub helps enforce security best practices. Identifying and rectifying potential security issues early in the development lifecycle is essential to ensure the confidentiality and integrity of APIs.

3. **Preventing Data Leaks:** By systematically scanning SwaggerHub for sensitive information, organizations can proactively prevent data leaks. This is especially crucial in today's interconnected digital landscape where APIs play a vital role in data exchange between services.

4. **Risk Mitigation:** Understanding that developers might forget to remove or obfuscate sensitive details in API documentation underscores the importance of continuous OSINT on SwaggerHub. This proactive approach mitigates the risk of unintentional exposure of critical information.

5. **Compliance and Privacy:** Many industries have stringent compliance requirements regarding the protection of sensitive data. OSINT on SwaggerHub ensures that APIs adhere to these regulations, promoting a culture of compliance and safeguarding user privacy.

6. **Educational Opportunities:** Identifying oversights in SwaggerHub documentation provides educational opportunities for developers. It encourages a security-conscious mindset, fostering a culture of awareness and responsible information handling.

By recognizing that developers can inadvertently expose secrets, OSINT on SwaggerHub becomes an integral part of the overall security strategy, safeguarding against potential threats and promoting a secure API ecosystem.


## How SwaggerSpy Works

SwaggerSpy obtains information from SwaggerHub and utilizes regular expressions to inspect API documentation for sensitive information, such as secrets and credentials.

## Getting Started

To use SwaggerSpy, follow these steps:

1. **Installation:** Clone the SwaggerSpy repository and install the required dependencies.

```bash
git clone https://github.com/your-username/SwaggerSpy.git
cd SwaggerSpy
pip install -r requirements.txt
```

2. **Usage:** Run SwaggerSpy with the target SwaggerHub URL.

```bash
python swaggerspy.py searchterm
```

3. **Results:** SwaggerSpy will generate a report containing OSINT findings, including information about the API, endpoints, and secrets.

## Disclaimer

SwaggerSpy is intended for educational and research purposes only. Users are responsible for ensuring that their use of this tool complies with applicable laws and regulations.

## Contribution

Contributions to SwaggerSpy are welcome! Feel free to submit issues, feature requests, or pull requests to help improve this tool.

## About the Author

SwaggerSpy is developed and maintained by *Alisson Moretto* (UndeadSec)

I'm a passionate cyber threat intelligence pro who loves sharing insights and crafting cybersecurity tools.

Consider following me:

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/alissonmoretto)
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/UndeadSec)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/UndeadSec)

## TODO

### Regular Expressions Enhancement

- [ ] Review and improve existing regular expressions.
- [ ] Ensure that regular expressions adhere to best practices.
- [ ] Check for any potential optimizations in the regex patterns.
- [ ] Test regular expressions with various input scenarios for accuracy.
- [ ] Document any complex or non-trivial regex patterns for better understanding.
- [ ] Explore opportunities to modularize or break down complex patterns.
- [ ] Verify the regular expressions against the latest specifications or requirements.
- [ ] Update documentation to reflect any changes made to the regular expressions.

## License

SwaggerSpy is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Thanks

Special thanks to [@Liodeus](https://github.com/Liodeus) for providing project inspiration through [swaggerHole](https://github.com/Liodeus/swaggerHole).
