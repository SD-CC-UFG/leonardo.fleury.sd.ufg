import EventEmitter fom 'events'
import axios from 'axios'

class NoteAPI extends EventEmitter {
    constructor() {
        super()

        this.ref = axios.create({
            baseURL: 'http://127.0.0.1:5000'
        })
        this.attachAxiosListeners()
    }

    // creates a note
    create({ content = '' }, onComplete) {
        this.ref.post('/', {
            content: this.content
          })
            .then(response => {})
            .catch(e => {
              this.errors.push(e)
              console.error(e)
            })
    }
    // updates a note
    update({ key, content = '' }, onComplete) {

    }
    // removes a note
    remove({ key }, onComplete) {

    }
    // attach listeners to Axios
    attachAxiosListeners() {
        this.ref.on('child_added', this.onAdded, this)
        this.ref.on('child_removed', this.onRemoved, this)
        this.ref.on('child_changed', this.onChanged, this)
    }
    // dettach listeners from Axios
    detachAxiosListeners() {
        this.ref.off('child_added', this.onAdded, this)
        this.ref.off('child_removed', this.onRemoved, this)
        this.ref.off('child_changed', this.onChanged, this)
    }
    onAdded() {
        // process data
        
        // propagate event outwards with note
        this.emit('added', note)
    }
    onRemoved() {
        
        this.emit('removed', note)
    }
    onChanged() {
        
        this.emit('changed', note)
    }
}

export default new NoteAPI()