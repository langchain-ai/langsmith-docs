import React, { useEffect } from 'react';
import { useHistory } from '@docusaurus/router';

export default function ChildPage() {
  const history = useHistory();

  useEffect(() => {
    // Redirect to parent page on load
    history.push('../how_to_guides');
  }, [history]);

  return null; // No need to render anything since we're redirecting
}