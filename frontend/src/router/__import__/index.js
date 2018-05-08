const path = process.env.NODE_ENV === 'production' ? 'production' : 'development'
const __import__ = require(`./_import_${path}`)

/**
* in development-env not use lazy-loading, because lazy-loading too many pages will
* cause webpack hot update too slow. so only in production use lazy-loading;
*/

export default __import__
