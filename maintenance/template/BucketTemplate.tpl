# {{ repo.full_name }}

* **Repository:** [{{ repo.html_url }}]({{ repo.html_url }})
* **Score:** {{ repo.score }}
* **Auto-Update:** {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}%
{% if ecosystem_name == 'scoop_shovel' %}
{% if repo.is_scoop_official %}* **Status:** 👑 Official Scoop Bucket{% elif repo.is_scoop_known %}* **Status:** ⭐ Known Scoop Bucket{% endif %}
{% if repo.is_shovel_official %}* **Status:** 👑 Official Shovel Bucket{% elif repo.is_shovel_known %}* **Status:** ⭐ Known Shovel Bucket{% endif %}
{% else %}
{% if repo.is_scoop_official %}* **Status:** 👑 Official Repository{% endif %}
{% endif %}

## 📦 Recipes ({{ repo.entries|length }})
{% for entry in repo.entries -%}
  * [{{ entry.split('/')[-1] }}]({{ repo.html_url }}/blob/{{ repo.default_branch }}/{{ entry }})
{% endfor -%}