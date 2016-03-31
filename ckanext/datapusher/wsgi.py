import ckanserviceprovider.web as web
import datapusher.jobs as jobs
import logging
log = logging.getLogger(__name__)
# check whether jobs have been imported properly
assert(jobs.push_to_datastore)

web.init()

#log.info('DDDebug{0}',web.app.config.get('HOST'))
web.app.run(web.app.config.get('HOST'), web.app.config.get('PORT'))

