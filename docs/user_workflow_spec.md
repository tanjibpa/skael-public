Please refer to the user workflow that has been shared in Slack (or has been mailed to you). We are hoping the final design document would become something like the [attached image](skael/docs/skael_user_org_flow.png).

Currently, we have basic APIs to user creation, verification, login, logout with JWT token based authentication.

## Organization

The first thing when we register a customer is to create an organization. An organization can only be created by Skael admin. This detail comes through Sales channel. Each organization will have its corresponding adddress. There is currently 1-1 relationship between organization and address.

For a start, we would need migration for organization "Skael" with id = 1 and corresponding address with id = 1 set. It will always be 1 for Skael Organization

An organization could be one or many "organization type". To begin with, we will have three organization type: Skael, Customer, Supplier. Of course, only Skael organization can be of type Skael. Rest would be either Customer or Supplier or both.

## Users

Similarly to Organization, we need to add the first skael admin with id = 1. This should also go as migration really so that we can propagate this to every new system (staging/production).


## Integration

In Skael, each organization will let us integrate with their ERP/Salesforce etc accounts so that we can pull/push data. The first thing an organiztion admin does is provide details of each integration. Integration detail can just be a JSON blob which will have connection details pertaining to a type. This way we can extend as we need.


## User initiation

In Skael view of world, Skael admin creates an organization and creates a user with admin role in backend with a temporary generated password. This sends a  mail to the admin through which he verifies his account. The first thing he does is reset the password. So the verify API has to be updated to do password reset too. A user **cannot** verify his account without resetting his password.

Once resetting his password, users can do their task based on roles.


## RBAC


An organization can be of a type. Each type has selected roles. So we have to design a DB that has the following features:

* Organization maybe of multiple types
* A user in an organization can have one or more roles of that type.
* Need/Permission Name
* A user can have series of permissions. In my past job as Rails developer I have had good usage with [CanCan](https://github.com/ryanb/cancan). We could use [Flask-Rbac](https://flask-rbac.readthedocs.io/en/latest/) or implement our own custom way.

Currently, two type that needs to be created as data migration:

* Customer with roles: Basic, Procurement, Executive, Admin
* Supplier with roles: Sales, Executive, Admin
