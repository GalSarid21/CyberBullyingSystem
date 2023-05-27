import React from 'react'
import {Route, Routes} from 'react-router-dom'

import DbManagementPage from './pages/DbManagement';
import ProjectPage from './pages/Project';
import NlpModelPage from './pages/NlpModel';
import Layout from './components/layouts/Layout';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path='/' element={<ProjectPage />} />
        <Route path='/nlp-model' element={<NlpModelPage />} />
        <Route path='/db-management' element={<DbManagementPage />} />
      </Routes>
    </Layout>
  );
}

export default App;
