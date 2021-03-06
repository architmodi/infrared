# FIXME(aopincar): This plugin should be in a type of its own
plugin_type: other
subparsers:
    collect-logs:
        description: Collect log from all nodes of the active workspace.
        include_groups: ["Ansible options", "Common options"]
        options:
          dest-dir:
              type: Value
              help: Path to a destination directory where the collected log will be stored
          archive-custom:
              type: Value
              help: Comma,separated list of additional path(s) to be archived.
          gzip:
              type: Bool
              help: |
                  Whether using gzip to archive or not
                  When used - output files will be suffixed with ".gz"
              default: False
          max-depth:
              type: Value
              help: Number of levels to descend at most when collecting logs
              default: 4
          logger:
              type: Value
              help: |
                    Specifies which facility we are using for log collection:
                        * host - gather and fetch log files from the system
                        * sosreport - use sosreport utility to get logs
                        * all -  use both variants
              choices: ['host', 'sosreport', 'all']
              default: 'host'