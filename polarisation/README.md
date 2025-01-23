# Corpus Polarisation de l'Espace Public

The version of this dataset published within the `papers/2021-IC2S2` directory corresponds to the article accessible here: https://arxiv.org/abs/2107.12073

## Summary

*Resources*

* [Medias](#medias)

<h2 id="medias">Medias</h2>

File: [medias.csv](./medias.csv)

A list of French medias that we study on the Internet.

*Fields*

* **webentity_id** (*integer*): Webentity ID for the media, as given by Hyphe in the original corpus.
* **name** (*string*): Media name.
* **prefixes** (*string*): List of urls separated by '|' and defining the limits of the media's webentity in Hyphe.
* **home_page** (*string*): The media's webentity home page as was defined in Hyphe.
* **start_pages** (*string*): List of urls separated by '|' and that served as starting pages for the media's webentity crawl in Hyphe.
* **indegree** (*integer*): Indegree of the media's webentity in the original Hyphe corpus.
* **hyphe_creation_timestamp** (*integer*): Timestamp of the media's webentity creation in Hyphe.
* **hyphe_last_modification_timestamp** (*integer*): Timestamp of the media's webentity last modification in Hyphe.
* **outreach** (*string*): The media's outreach, e.g. national, regional etc.
* **foundation_year** (*year*): Year the media was founded.
* **batch** (*integer*): Batch number when the media was added to the corpus.
* **edito** (*string*): The media's editorialization.
* **parody** (*boolean*): Whether the media's contents are parodical.
* **origin** (*string*): Media national origin.
* **digital_native** (*boolean*): Whether the media is digital native.
* **mediacloud_ids** (*string*): List of the media's ids on the Media cloud platform, separated by '|'.
* **wheel_category** (*string*): Media category as inferred by SBM hierarchical clustering.
* **wheel_subcategory** (*string*): Media subcategory as inferred by SBM hierarchical clustering.
* **has_paywall** (*boolean*): Whether the media has a paywall on its website.
* **inactive** (*boolean*): Whether the media can now be considered as inactive.
