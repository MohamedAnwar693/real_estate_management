Custom Odoo Module To Manage Real Estate
Real Estate Management Custom Odoo Module
This is a custom Odoo module designed for real estate management. It integrates core functionalities to manage properties, agents, tenants, leases, sales, and amenities. The module provides a comprehensive suite of features to facilitate property management for real estate businesses, property owners, and agents.

Features
Property Management: Manage real estate properties, including details such as address, type, status, price, and more.
Agent Management: Keep track of agents and their assigned properties, commissions, and performance.
Amenity Management: Define and manage amenities available for properties (e.g., swimming pool, gym, etc.).
Lease Management: Track and manage tenant leases, including terms, payment schedules, and renewal options.
Sale Management: Manage property sales, including buyer details, transaction history, and payment status.
Tenant Management: Store and manage tenant information, including lease agreements, payment records, and communication history.
Models
This module includes the following Odoo models:

1. Property
Represents real estate properties available for rent or sale.
Fields:
name (Char): Property name.
address (Text): Property address.
property_type (Selection): Type of property (e.g., House, Apartment, Office).
price (Float): Sale or rent price.
status (Selection): Current status of the property (e.g., Available, Sold, Rented).
agent_id (Many2one): Associated agent handling the property.
2. Agent
Represents real estate agents responsible for managing properties.
Fields:
name (Char): Agent name.
phone (Char): Contact phone number.
email (Char): Contact email address.
assigned_property_ids (One2many): Properties assigned to the agent.
commission_rate (Float): Commission percentage for each transaction.
3. Amenity
Represents amenities available in properties.
Fields:
name (Char): Amenity name (e.g., Swimming Pool, Gym).
description (Text): Detailed description of the amenity.
property_ids (Many2many): Properties that offer this amenity.
4. Lease
Represents lease agreements between tenants and property owners.
Fields:
tenant_id (Many2one): Tenant associated with the lease.
property_id (Many2one): Property leased by the tenant.
start_date (Date): Lease start date.
end_date (Date): Lease end date.
monthly_rent (Float): Monthly rental price.
payment_schedule (Selection): Payment terms (e.g., Monthly, Quarterly).
5. Sale
Represents sale transactions for properties.
Fields:
property_id (Many2one): Property sold.
buyer_name (Char): Name of the buyer.
sale_price (Float): Sale price of the property.
sale_date (Date): Date of the sale transaction.
payment_status (Selection): Payment status (e.g., Paid, Pending).
6. Tenant
Represents tenants renting properties under lease agreements.
Fields:
name (Char): Tenant name.
email (Char): Tenant email address.
phone (Char): Tenant phone number.
leased_property_ids (One2many): Properties leased by the tenant.
lease_ids (One2many): Lease agreements associated with the tenant.
Installation
To install this module, follow these steps:

Download or clone the module to your Odoo instance's addons directory.
Update the app list in Odoo.
Install the "Real Estate Management" module from the Odoo apps menu.
Configuration
After installation, you can configure the following:

Properties: Add properties with details like address, price, and type.
Agents: Assign agents to properties and set commission rates.
Amenities: Define available amenities and associate them with properties.
Leases and Sales: Create lease and sale transactions, link them to tenants and properties.
Usage
Managing Properties
Go to the "Properties" menu to view and manage available properties.
Add new properties and associate them with agents and amenities.
Managing Agents
Under the "Agents" menu, you can add new agents and assign properties to them.
Agents can have their commissions tracked per transaction.
Lease and Sale Transactions
Under the "Leases" or "Sales" menu, create new lease or sale records, linking them to tenants, properties, and agents.
Tenant Management
Manage tenants by adding them under the "Tenants" menu. Keep track of their leases and payment records.
Contributing
If you wish to contribute to this module, feel free to fork the repository and submit pull requests. We welcome improvements and bug fixes.
