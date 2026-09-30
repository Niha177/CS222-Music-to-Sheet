import { useState } from 'react'

import './App.css'

function App() {
  const [file, setFile] = useState([])
  console.log(file)
  
  if(file != null) {
    console.log(file[0].name)
  }
  

  return(
    <main>
      <div>Drop Music File Here (.wav file only)</div>
      

      <input 
        type='file'
        accept='.wav'
        onChange={(e) => {
          const[file] = e.target.files;
          setFile((music) => [...music, file])
        }}

      />
      
      
    </main>
  )

  

  
}

export default App
