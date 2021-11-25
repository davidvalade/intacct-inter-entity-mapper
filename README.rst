===========================================
Intacct Inter-Entity Account Mapping Helper
===========================================


.. image:: https://img.shields.io/pypi/v/intacct_inter_entity_account_mapping_helper.svg
        :target: https://pypi.python.org/pypi/intacct_inter_entity_account_mapping_helper

.. image:: https://img.shields.io/travis/davidvalade/intacct_inter_entity_account_mapping_helper.svg
        :target: https://travis-ci.com/davidvalade/intacct_inter_entity_account_mapping_helper

.. image:: https://readthedocs.org/projects/intacct-inter-entity-account-mapping-helper/badge/?version=latest
        :target: https://intacct-inter-entity-account-mapping-helper.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/davidvalade/intacct_inter_entity_account_mapping_helper/shield.svg
     :target: https://pyup.io/repos/github/davidvalade/intacct_inter_entity_account_mapping_helper/
     :alt: Updates



A helper to assist with the GL account mappings required by Sage Intacct to track Due-to and Due-from transactions.


* Free software: MIT license
* Documentation: https://intacct-inter-entity-account-mapping-helper.readthedocs.io.


Features
--------

Sage Intacct has great functionality to track due-to and due-from balances. Thinking through the relationship isn't always obvious, so this can help.

Many different strategies for creating these accounts abound, but some are excessively complicated in environments with many entities. Sage Intacct once recommended having a different account for every entity's receivable from every other entity, and one payable as well. By that logic, we would need:

	X ( X - 1) ^ 2 accounts, where X = the number of entities.

That would mean for an environment with 150 entities we would need 44,700 accounts!

Going from 150 entities to 151 would mean having a total of 45,300 accounts (adding 600 GL accounts).

That is all too much. Instead, this program will recommend making two accounts for each entity. Going from 150 to 151 entities with our logic adds just 2 accounts. Better!

We still have complexity in the mapping, however. If you follow the recommended setup here, our mapping would have:

	(X ^ 2 - X) / 2 lines of mapping, where X = the number of entities.
	
So the mapping would have 11,175 rows for a 150 entity environment.

Fear not, this application will create a mapping file suitable for import into Sage Intacct.

The list of entities can be keyed, imported, or a dummy list of entities can be used to illustrate the mappings. Two files are created: a list of the unique GL Account placeholders and the CSV file. For this release, real GL account numbers are not used, but a VLOOKUP or find/replace to swap placeholders for real GL accounts would need to happen pre-upload.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
